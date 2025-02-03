> [!Warning]
> SMTPD (!Deprecated)
```bash
export EMAIL_HOST="localhost"
export EMAIL_PORT=1025

python -m smtpd -n -c DebuggingServer $EMAIL_HOST:$EMAIL_PORT
```
