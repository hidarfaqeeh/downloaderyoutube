
    # cloning the repo and installing requirements.
    && git clone https://github.com/hidarfaqeeh/downloaderyoutube.git/ \
    && pip3 install -r requirements.txt
&& python3 -m bot
worker : chmod +x start.sh && bash start.sh
