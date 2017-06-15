# reading mp3 meta data
import eyed3
# confirming the file exists
import os.path
import math
# used to get command line arguments
import sys
import time

if len(sys.argv) != 5:
    print 'Must call this python script with 4 parameters: filename, title, subtitle, and description'
    sys.exit()

filename = sys.argv[1]

if os.path.isfile(filename):
    podcast = eyed3.load(filename)
    number_of_bytes = podcast.info.size_bytes
    number_of_seconds = podcast.info.time_secs
    number_of_minutes = int(math.floor(number_of_seconds/60))
    number_of_seconds = number_of_seconds - (number_of_minutes*60)
    if number_of_seconds < 10:
        number_of_seconds = "0" + str(number_of_seconds)
    publish_date = time.strftime("%a, %d %b %Y 20:00:00 GMT")

    title = sys.argv[2]
    subtitle = sys.argv[3]
    description = sys.argv[4]

    xml_for_podcast = """
        <item>

      <title>%s</title>

      <itunes:author>David Rust-Smith and Nick Breen</itunes:author>

      <itunes:subtitle>%s</itunes:subtitle>

      <itunes:summary>%s</itunes:summary>
      <itunes:image href="http://davidrs.com/stealmyidea/podcast/steal-my-idea-album-picture.png" />

      <enclosure url="http://davidrs.com/stealmyidea/podcast/rw%s" length="%s" type="audio/mpeg" />

      <guid>http://davidrs.com/stealmyidea/podcast/%s</guid>

      <pubDate>%s</pubDate>

      <itunes:duration>%s:%s</itunes:duration>

    </item>
    """ % (title, subtitle, description, filename, number_of_bytes, filename, publish_date, number_of_minutes, number_of_seconds)

    print xml_for_podcast

else:
    print 'could not find a file named %s in this directory.' % (filename)
