# BotsForJeff

bots setup and instructions for  my bro Jeff

Clone and cd into the directory

```
git clone https://github.com/kneeraazon01/BotsForJeff
```

```
cd BotsForJeff
```

## Now create one virtual environment that works for both Discord and Telegram bots

```
python3 -m venv venv
```

### To activate the virtualenv in Linux/Mac

```
source venv/bin/activate
```

### For windows Operating System

```
Scripts\activate.bat
```

### Now install all the dependencies

```
pip install -r requirements.txt
```

## Telegram Bot Setup and Cofiguration

### Just run the following commands in your terminal

```
cd telegram-dm-bot
```

```
python setup.py -c
```

#### To scrape the users run

```
python scraper.py
```

#### Now you can run the sms bot with the following command

```
python smsbot.py
```

## To add members to groups run

```
cd llattes
```

```
python SessionCreator.py
```

```
python Scraper.py 
```

#### and pass the username/code of the group as shown in the video, which will be the username/code from an invitation link

### Now to add the members that have been scraped to members.txt to your group run

```
python MemberAdder.py
```

#### and provide the destination group as whosn in the video

#### That is all for the telegram bot
