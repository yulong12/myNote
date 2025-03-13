curl -X POST "http://10.5.5.25:30070/v1/chat/completions" \
-H "Content-Type: application/json" \
-d '{
  "model": "model_72B",
  "messages": [
    {"role": "system", "content": "你是一个人工助手."},
    {"role": "user", "content": "用简单的术语解释量子计算。"}
  ],
  "max_tokens": 300
}'