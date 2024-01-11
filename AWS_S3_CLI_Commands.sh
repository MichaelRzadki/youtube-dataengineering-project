#Upload Data to S3 Bucket:
#Go to the location/path where the Kaggle data was downloaded and run the following command to upload json data.
aws s3 cp . s3://dataeng-on-youtube-raw-dev/youtube/raw_statistics_reference_data/ --recursive --exclude "*" --include "*.json"

#Upload the remaining csv files based on country using the follow commands
aws s3 cp CAvideos.csv s3://dataeng-on-youtube-raw-dev/youtube/raw_statistics/region=ca/
aws s3 cp DEvideos.csv s3://dataeng-on-youtube-raw-dev/youtube/raw_statistics/region=de/
aws s3 cp FRvideos.csv s3://dataeng-on-youtube-raw-dev/youtube/raw_statistics/region=fr/
aws s3 cp GBvideos.csv s3://dataeng-on-youtube-raw-dev/youtube/raw_statistics/region=gb/
aws s3 cp INvideos.csv s3://dataeng-on-youtube-raw-dev/youtube/raw_statistics/region=in/
aws s3 cp JPvideos.csv s3://dataeng-on-youtube-raw-dev/youtube/raw_statistics/region=jp/
aws s3 cp KRvideos.csv s3://dataeng-on-youtube-raw-dev/youtube/raw_statistics/region=kr/
aws s3 cp MXvideos.csv s3://dataeng-on-youtube-raw-dev/youtube/raw_statistics/region=mx/
