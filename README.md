# Subscription Parser

## Use to parse through the raw .csv provided by takeout.google.com for the [Youtube Subscriptions Importer Extension for chrome](https://chrome.google.com/webstore/detail/subscriptions-importer-fo/dejjakoompaeblngfchggeaballjkmao)

### This will be a guide on how to utilise this script to transfer your youtube subscriptions from one google account to another if you don't feel like paying the 15$ the extension we'll be utilising charges for more than 50 subs at a time.

### First thing's first:

##### This guide assumes you have python 3 installed and an a basic idea of how to open a terminal or command prompt and run a python application

1. Clone this repository into your downloads folder, or wherever you want
2. Go to takeout.google.com while you're logged into the account you want to transfer the subs from
3. Click **Deselect all** in the top right of the page that pops up
4. Scroll all the way to the bottom of the page and click the checkmark next to the Youtube and Youtube music entry
5. Click **All YouTube data Included** and unselect everything but subscriptions and click **OK** then **Next Step**
6. Then choose the delivery mechanism for your files, you'll have to wait a few minutes while they generate your backup so be patient 😊
7. Once you've gotten your data then you're gonna wanna download then extract the .zip file.  

It should look something like this: ![Image of a zipfile that has been extracted](/assets/zipExtracted.png)

8. You'll then want to navigate to Takeout/YouTube and YouTube Music/subscriptions
9. You'll need to either copy or move the subscriptions.csv into the the directory of the repository that we cloned earlier
10. Then we'll need to open a console/ command prompt and change directories to the repository's folder, then type:

> pip install -r requirements.txt

11. Once you've completed that step, then you're gonna wanna install the [Youtube Subscriptions Importer Extension for chrome](https://chrome.google.com/webstore/detail/subscriptions-importer-fo/dejjakoompaeblngfchggeaballjkmao) and make sure that you're logged into google chrome with the account that you want to transfer the subs into.

11. Then open another console, or use the one we opened just 1 step ago and type the following and press enter:

> python subscriptionParser.py  

12. Assuming you've done everything correctly, on the first run of the program it should generate a file called **subscriptions.json** in the directory of the repository, this is normal, it will then ask you to input 2 numbers, your subscription list starts with 0 and ends with however many subs you have. Once you've entered the 2 numbers the program will have automatically copied all of the URLs to your clipboard in a form that the extension can parse.
13. Now that we have our URLs, click the extension you installed earlier(usually under the puzzle piece in the top right corner of chrome) and paste(Ctrl-V) the URLs into the box that says **Paste Exported Channels List here** scroll down and click import, then import on the next page.  

Now you'll definitely need to monitor this process as youtube for some reason keeps you subscribed to channels that have been banned, so you'll occasionally need to close the tab it opens and click **Unstuck Process**.

I recommend going 0-50 then 50-100 and so on as the extension can only handle 50 URLs at a time unless you pay 15$, and nobody has time for that shit, the program will eventually tell you that it couldn't parse all 50, at this point, you're done! So congratulations on circumventing capitalism.