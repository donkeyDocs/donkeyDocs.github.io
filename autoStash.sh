# git add . && git commit -am "Updated" && git push
#falls back on 500 seconds if no parameter is passed to the script
waitFor=${1:-500}
#this fetches the date

while true; do now=$(date); git stash; git pull; read -t $waitFor -p "Hit return to trigger now. Else will trigger later automatically."; done