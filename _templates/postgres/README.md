```bash
docker run \
  -d \
  -p 8475:5432 \
  -e POSTGRES_DB=templates__postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=simple \
  --restart unless-stopped \
  --name templates__postgres \
  postgres
```