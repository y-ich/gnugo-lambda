# GnuGo on AWS Lambda

AWS Lambda gives you the following free tier.
- 1M requests per month
- 3.2M seconds per month

Even if you spend 30 seconds to calculate score in aftermath by gnugo, you can provide GnuGo scoring service upto 106k requests per month for free!

## Install

1. Create a function on AWS Lambda from "Author fromm scratch".
1. upload gnu.zip
1. add API Gateway as trigger
1. setup API

That's all!

### License

MIT