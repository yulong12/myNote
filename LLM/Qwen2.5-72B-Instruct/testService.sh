# 使用NodePort方式访问（替换实际节点IP）
curl http://10.5.5.25:30070/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "/model",
    "prompt": "人工智能领域的最新突破是",
    "max_tokens": 100,
    "temperature": 0.7
  }'
