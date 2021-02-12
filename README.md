# Week3Exercise4

To build the image, run Docker build from a command line or terminal that is in the root directory of the application.

  $docker build -t <image-name> .

After it is built, you can run the script with an argument
  
  $ docker run -d -p 84:80 <image-name> python /src/hello.py <any name/ word>
