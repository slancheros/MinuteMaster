---
description: We have created a docker image for your convenience
---

# Set up

Also the convenience of having the audio conversion readily available wherever it runs

You can build the container running the following command:

```
docker build . -t gradio_app
```

To run the container you can use this one:

```
docker run --rm -it -p 7862:7860 --name gradio_container gradio_ap
```

On your local browser you can reach the Gradio application on&#x20;



```
http://localhost:7862
```
