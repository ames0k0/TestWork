Fixing the text-indent overflow for: https://www.kasuga100.com
![text-indent issue](static/issue.png)
```css
.slick-arrow {
  <!-- FIXFOR: *text-indent overflow after `slick-next` transform rotate -->
  overflow: hidden;
}
```
- [x] Fixed by: https://stackoverflow.com/a/29806966
- [x] Fixing process: https://youtu.be/KaGB5KFf54s
