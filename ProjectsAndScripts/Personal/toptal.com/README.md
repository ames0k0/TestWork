# [TopTal](https://toptal.com)
Get `.gitignore` file
```bash
if [ "$1" == '' ];
then
  echo 'gitignore [lang]'
else
  curl "https://www.toptal.com/developers/gitignore/api/{$1}" > .gitignore
fi
```

- [ ] TODO