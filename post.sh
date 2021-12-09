# curl -X POST -F 'sql=select * from film' localhost:5000/dvdrental/
curl -X POST -H "Content-Type: application/json"  --data '{"sql":"select * from film"}' localhost:5000/dvdrental/
