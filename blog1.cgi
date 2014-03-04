#!/usr/local/bin/ruby
# -*- coding: utf-8 -*-

require 'cgi'
require 'pg'

conn = PGconn.connect(dbname: 'blogsystem', user: 'postgres')

result = conn.exec("select * from post;")
value = result.getvalue(0,0)

cgi = CGI.new

puts cgi.header("charset"=>"utf-8")
print <<EOM
<html>
<head>
  <title>簡易ブログ</title>
</head>
<body>
  <h1>ブログ的なあれ</h1>
  <hr>
EOM

result.each do |i|
  print "<p>#{i['title']}</p><p1>#{i['main']}</p1>"
end

print <<EOM
  <form action="upgrate.cgi" method="get">
    <p>
    名前:<input type="text" name="usr1" /><br />
    <textarea name="text1" rows="8" cols="40"></textarea><br />
    <input type="submit" name="button2" value="送信" />
    </p>
  <form>
  <hr>
  <br>
EOM

result.clear

conn = PGconn.connect(dbname:"blogsystem", user:"postgres")
result = conn.exec("select * from comment")

print <<EOM

  <form action="upgrate.cgi" method="get">
    <p>
    名前:<input type="text" name="usr2"><br>
    コメント<br>
    <textarea name="comment" rows="8" cols="40"></textarea><br>
    <input type="submit" name="button1" value="送信">
    </p>
  </form>
EOM

puts '<table border="1">'
puts '<caption>コメント</caption>'
puts '<tr><th>投稿者</th><td></td></tr>'

result.each do |i|
  print "<tr><th>#{i['viewer']}<th><td>#{i['content']}</td> </tr>"
end

puts '</table>'

puts '</body>'
puts '</html>'

