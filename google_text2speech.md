# Google Text to Speech API
Base URL: http://translate.google.com/translate_tts  
It converts written words into audio. It accepts `GET` requests.

## GET
`q`  
The query string to convert to audio

`tl`  
Translation language, for example, `ar` for Arabic, or `en-us` for English

`ie`  
Encoding format, use default `UTF-8`

## Examples

### This is an example for Arabic "السلام عليكم"

    http://translate.google.com/translate_tts?ie=UTF-8&q=%D8%A7%D9%84%D8%B3%D9%84%D8%A7%D9%85%20%D8%B9%D9%84%D9%8A%D9%83%D9%85&tl=ar

### This is an example for English "Hello World"

    http://translate.google.com/translate_tts?ie=UTF-8&q=Hello%20World&tl=en-us