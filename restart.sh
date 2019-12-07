if [ $# -eq 0 ]; then
    echo '##### git pull #####'
    git pull
fi

if [ $1 != '--local' ]; then
    exit 1
fi

echo '##### Restart Docker container #####'
docker-compose down
docker-compose build
docker image prune -f
docker-compose up -d
