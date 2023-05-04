#!/bin/bash

python3 -m fastchat.serve.controller \
            --host 127.0.0.1 \
            --port $FASTCHAT_CONTROLLER_PORT &

python3 -m fastchat.serve.model_worker \
            --host 0.0.0.0 \
            --port $FASTCHAT_WORKER_PORT \
            --model-name $MODEL_NAME \
            --model-path $MODEL_PATH \
            --device $FASTCHAT_DEVICE \
            --num-gpus $FASTCHAT_GPU_COUNT \
            --controller-address http://0.0.0.0:$FASTCHAT_CONTROLLER_PORT &

python3 -m fastchat.serve.api \
            --host 0.0.0.0 \
            --port $FASTCHAT_API_PORT
