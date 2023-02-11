obs&
sleep 5
xdotool key Tab
sleep 0.5
xdotool key Tab
sleep 0.5
xdotool key Tab
sleep 0.5
xdotool key Tab
sleep 0.5
xdotool key Tab
sleep 0.5
xdotool key Tab
sleep 0.5
xdotool key Tab
sleep 0.5
xdotool key Tab
sleep 0.5
xdotool key Tab
sleep 0.5
xdotool key Tab
sleep 0.5
xdotool key Tab
sleep 0.5

xdotool key space
sleep 0.5

xdotool key Down
sleep 0.5

xdotool key Tab
sleep 0.5
xdotool key Tab
sleep 0.5

# reset to choose ingest
for ((re=1;re<=65;re++))
do
xdotool key Up
sleep 0.2
done
xdotool key Down
sleep 0.5


xdotool key Tab
sleep 0.5
xdotool key Tab
sleep 0.5
xdotool key Tab
sleep 0.5
xdotool key Tab
sleep 0.5
xdotool key Tab
sleep 0.5
xdotool key Tab
sleep 0.5

xdotool key space
sleep 0.5

sleep 1
pidof obs | xargs kill
sleep 1
# obs disconnect