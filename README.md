# askiiart/http-codes

HTTP status codes for nginx, but better.

## Original post

Collection of HTTP status codes, from [@yassie_j@0w0.is](https://0w0.is/yassie_j) and a couple others:

- 403 [You Shall Not Pass](https://0w0.is/notice/AZpeq9kdiVbKocpo0m)
- 301 [Your Princess in in Another Castle](https://0w0.is/notice/AZpfAtcGtx1gr4oHVg)
- 451 [Oi, You Got a Loicense For That Mate?](https://0w0.is/notice/AZpfQAPElAI5GszkAa)
- 204 [Head Empty No Thoughts](https://0w0.is/notice/AZpfdFJboofeGHbCUa)
- 402 [Come Back When You're a Little MMMMM Richer](https://0w0.is/notice/AZpfvcOck8SL3fhmwS)
- 413 [Me After A Night With Your Mother](https://0w0.is/notice/AZpgMXPNObkTPJtSKW)
  - 417 me after 20-something years with my mother (from [Evvy](https://tech.lgbt/@pierogiburo/111076180358295709))
- 502 [Forgive Me Father For My Gateway Has Sinned](https://0w0.is/notice/AZpgs0f6gIa775G4DQ)
  - 504 Note: Gateway died on the way back to its home planet (from [spectrums i'm on: at least two](https://realworldsunny.name/notes/9k8j3jo5hf))
- [508 508 508 508 508 508 508 508 508 508 508 508 508 508 508](https://0w0.is/notice/AZph3gHkGe5BOHtdJo)
- 418 [I'm A Teapot](https://0w0.is/notice/AZph69mBakLHR0JbVY)
    (this is just the real one)
- 410 [Your Father](https://0w0.is/notice/AZphDH230s43xu7zxQ)
- 406 [I Can't Believe You've Done This](https://0w0.is/notice/AZphGgRsyF6Zf8q71c)
- 401 [This Is Against TOS You've Been
    Reported](https://0w0.is/notice/AZphX4T5R1ksn5DPxA)
- 425 [Sorry This Never Happens With Other
    Women](https://0w0.is/notice/AZphi280TWwAicaBVI)
- 202 [You In My Heart](https://0w0.is/notice/AZpiODVUYkViAigMfA)
- 300 [Poll](https://0w0.is/notice/AZpicIzowoUZFaaPdg)
  - 57% Yes
  - 43% No
  - (300 Multiple Choices is the actual error code? Geddit?)
- 404 [You Made A Typo In The URL Didn't You](https://0w0.is/notice/AZpik5MrV9JpId4cTI)
- 423 [Fine Then Keep Your Secrets](https://0w0.is/notice/AZpj18ZUqKTa9u78Pg)
- 429 [i'm scared stop asking me q.q](https://meow.woem.cat/notes/9lgiyx2aahggxb4d)

## nginx rule

```nginx
error_page 300 /error/300.html;
error_page 301 /error/301.html;
error_page 401 /error/401.html;
error_page 402 /error/402.html;
error_page 403 /error/403.html;
error_page 404 /error/404.html;
error_page 406 /error/406.html;
error_page 410 /error/410.html;
error_page 413 /error/413.html;
error_page 417 /error/417.html;
error_page 418 /error/418.html;
error_page 423 /error/423.html;
error_page 425 /error/425.html;
error_page 429 /error/429.html;
error_page 451 /error/451.html;
error_page 502 /error/502.html;
error_page 508 /error/508.html;
```
