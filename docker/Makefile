
build:
	cd ..; docker build -t runnerly/tokendealer -f docker/Dockerfile .

run:
	docker run --net=runnerly --name=tokendealer -v /tmp/logs:/logs -p 8080:8080 -it runnerly/tokendealer
