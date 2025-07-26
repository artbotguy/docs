Токен аутентификации:

    {{ https://security.stackexchange.com/questions/166724/should-i-use-csrf-protection-on-rest-api-endpoints }}

    Хранени данных:
        В Local Storage:
            - может подвергаться XSS-атакам
        В сессии: 
            - может подвергаться CSRF-атакам
            - при установке HttpOnly-флага невозможна XSS-атака


Куки: 
    Безопасный способ установка:

        Secure;
            "Безопасные" (secure) куки отсылаются на сервер только тогда, когда запрос отправляется по протоколу SSL и HTTPS;
            Незащищённые сайты (http:) не могут создавать куки с флагом Secure

        HttpOnly;
            Куки HTTPonly не доступны из JavaScript - защищает от XSS-атак

        SameSite=(Strict | Lax | None);
            Отправка кук только тому сайту, которому они принадлежат



*************************************************************************



***
[Origin <protocol://hostname:port>]
  Отправляется клиентом только по http-запросам POST (?)
  Это простой заголовок, который указывает, откуда возник запрос. В отличие от Referer,
  этот заголовок также присутствует в HTTPS-запросах, в дополнение к HTTP-запросам. 
  Сервер проверяет допустим ли даный Origin и должен вернуть Access-Control-Allow-Origin, 
  а клиент его проверить.

[Referer <protocol://hostname:port>]
  Задается клиентом для всех запросов, а также указывает, откуда возник запрос. 
  Единственный раз, когда этот заголовок отсутствует, это когда ссылающаяся ссылка имеет 
  атрибут rel=noreferer.

***
[Access-Control-Allow-Origin]

*************************************************************************

ПРОСТЫЕ ЗАПРОСЫ [GET | POST | HEAD]
  {Заголовки запросов}
      Accept
      Accept-Language
      Content-Language
      Content-Type [application/x-www-form-urlencoded | multipart/form-data | text/plain]
  {Заголовки ответов}
      Cache-Control
      Content-Language
      Content-Type
      Expires
      Last-Modified
      Pragma

Чтобы разрешить JavaScript доступ к любому другому заголовку ответа, 
сервер должен указать заголовок Access-Control-Expose-Headers
  




