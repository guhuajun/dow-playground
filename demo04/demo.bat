docker run -it greggu/demo04
docker run -it --volumes-from demo0401 greggu/demo04

REM Read-only mode
docker run -it --volumes-from demo0401:ro greggu/demo04