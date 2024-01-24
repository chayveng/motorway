# Motorway Service

## Start All Services

```bash
docker compose up
```

## Start NGINX

```bash
cd nginx_server
docker compose up
```

## Start Fast API

```bash
cd fast_api
docker compose up
```

## Note

- Change domain api in nginx.conf ```server <YOUR_DOMAIN>:7357;```
