# Database Performance Testing

## Getting started
You will need

- A PostGIS database with your data and the credentials. If possible, use your team's staging database.
- Docker hosting.
- A Civic platform backend repository. For this document, we'll use `2019-transportation-systems-backend` but any of
them should work.

Setup:

1. Set the database credentials in `.env` at the root of the repository. The easiest way to do this is to copy `env.sample` to `.env` and then edit `.env`.

2. At the command line type `bin/build.sh -d`. This will build a Docker image.

3. When the build finishes, type `bin/start.sh -d`. This will start an API container connected to the database. You
should see something like this:

```
api_1  | Run server...
api_1  | [2019-09-05 03:36:50 +0000] [16] [INFO] Starting gunicorn 19.9.0
api_1  | [2019-09-05 03:36:50 +0000] [16] [INFO] Listening at: http://0.0.0.0:8000 (16)
api_1  | [2019-09-05 03:36:50 +0000] [16] [INFO] Using worker: sync
api_1  | [2019-09-05 03:36:50 +0000] [16] [INFO] Server is ready. Spawning workers
api_1  | [2019-09-05 03:36:50 +0000] [19] [INFO] Booting worker with pid: 19
```

## Exercising the API
1. Browse to your API. It should be accessible via the Swagger UI at `http://localhost:8000/<project>/v1/schema/`, where `<project>` is your project name. For this demo, it's `transportation2019`.
2. Pick the API endpoint you want to test. For this demo, I'm going to pick one that accesses a large table. The plan
is to start with small pages (`limit=20`) and increase by a factor of ten till it crashes. The query is "disturbance
stops for September 2018".

    For `limit=20`, the console running `bin/start.sh -d` shows:

    ```
    api_1  | (0.316) SELECT COUNT(*) AS "__count" FROM "disturbance_stops" WHERE ("disturbance_stops"."month" IN (9) AND "disturbance_stops"."year" IN (2018)); args=(9, 2018)
    api_1  | (0.197) SELECT "disturbance_stops"."opd_date", "disturbance_stops"."service_key", "disturbance_stops"."year", "disturbance_stops"."month", "disturbance_stops"."day", "disturbance_stops"."day_of_week", "disturbance_stops"."act_arr_time", "disturbance_stops"."act_dep_time", "disturbance_stops"."start_quarter_hour", "disturbance_stops"."end_quarter_hour", "disturbance_stops"."duration", "disturbance_stops"."line_id", "disturbance_stops"."pattern_direction", "disturbance_stops"."longitude", "disturbance_stops"."latitude", "disturbance_stops"."geom_point_4326"::bytea, "disturbance_stops"."id" FROM "disturbance_stops" WHERE ("disturbance_stops"."month" IN (9) AND "disturbance_stops"."year" IN (2018))  LIMIT 20; args=(9, 2018)
    api_1  | 172.18.0.1 [05/Sep/2019:03:51:53 +0000] GET /transportation2019/v1/toad/disturbanceStops/ limit=20&months=9&years=2018 HTTP/1.1 200 8895 http://localhost:8000/transportation2019/v1/schema/ Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0 1.551047
    ```

    Note that Django is doing two queries: the first counts all the rows, and the second returns the first `limit` rows. If you look at the response you'll see a link to the next page! The count returned is 1,476,835 - there were almost 1.5 million disturbance stops in September 2018.

3. Now multiply `limit` by 10 and keep going until it crashes. For this demo, 20,000 works and 200,000 crashes.

    ```
    api_1  | (0.265) SELECT COUNT(*) AS "__count" FROM "disturbance_stops" WHERE ("disturbance_stops"."month" IN (9) AND "disturbance_stops"."year" IN (2018)); args=(9, 2018)
    api_1  | (5.487) SELECT "disturbance_stops"."opd_date", "disturbance_stops"."service_key", "disturbance_stops"."year", "disturbance_stops"."month", "disturbance_stops"."day", "disturbance_stops"."day_of_week", "disturbance_stops"."act_arr_time", "disturbance_stops"."act_dep_time", "disturbance_stops"."start_quarter_hour", "disturbance_stops"."end_quarter_hour", "disturbance_stops"."duration", "disturbance_stops"."line_id", "disturbance_stops"."pattern_direction", "disturbance_stops"."longitude", "disturbance_stops"."latitude", "disturbance_stops"."geom_point_4326"::bytea, "disturbance_stops"."id" FROM "disturbance_stops" WHERE ("disturbance_stops"."month" IN (9) AND "disturbance_stops"."year" IN (2018))  LIMIT 200000; args=(9, 2018)
    api_1  | [2019-09-05 03:55:57 +0000] [16] [CRITICAL] WORKER TIMEOUT (pid:19)
    api_1  | [2019-09-05 03:55:57 +0000] [19] [INFO] worker received SIGABRT signal
    api_1  | [2019-09-05 03:55:57 +0000] [19] [INFO] Worker exiting (pid: 19)
    api_1  | [2019-09-05 03:55:57 +0000] [19] [INFO] worker exit signal
    api_1  | [2019-09-05 03:55:58 +0000] [22] [INFO] Booting worker with pid: 22
    api_1  | (0.247) SELECT COUNT(*) AS "__count" FROM "disturbance_stops" WHERE ("disturbance_stops"."month" IN (9) AND "disturbance_stops"."year" IN (2018)); args=(9, 2018)
    ```

    It will keep trying and keep timing out. Type `CTL-C` to put it out of its misery.
 
