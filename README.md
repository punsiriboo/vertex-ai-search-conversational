# vertex-ai-search-conversational
![Title](images/titile.png)
# Product Search - Vertex Search AI 

### 1. Create a GCS bucket (replace with your desired bucket name and location) 
```
export YOUR_BUCKET_NAME=XXXX
export YOUR_BUCKET_LOCATION=asia-southeast1

gsutil mb -l $YOUR_BUCKET_LOCATION gs://$YOUR_BUCKET_NAME
```

#### 2. Upload the data file to the bucket
```
gsutil cp data_store/funds.ndjson gs://$YOUR_BUCKET_NAME/data_store/product_retails_search.ndjson
```


### 3. Check file existing
```
gsutil ls gs://$YOUR_BUCKET_NAME/data_store/funds.ndjson
```

### 4. Goto Vertex AI Search Page in Your Google Cloud Project 
1. Create Vertex AI Seatch 
2. Create DataStore from GSC 
3. Setting the Search Agent


# Fund Search - Vertex Search AI 
Step: 

### 1. Create a GCS bucket (replace with your desired bucket name and location) 
```
export YOUR_BUCKET_NAME=XXXX
export YOUR_BUCKET_LOCATION=asia-southeast1

gsutil mb -l $YOUR_BUCKET_LOCATION gs://$YOUR_BUCKET_NAME
```

#### 2. Upload the data file to the bucket
```
gsutil cp data_store/funds.ndjson gs://$YOUR_BUCKET_NAME/data_store/funds.ndjson
```

### 3. Check file existing
```
gsutil ls gs://$YOUR_BUCKET_NAME/data_store/funds.ndjson
```

### 4. Goto Vertex AI Search Page in Your Google Cloud Project 
1. Create Vertex AI Seatch 
2. Create DataStore from GSC 
3. Setting the Search Agent

#### Instruction:
- Summary the NAV the fund detail and provide recommendation based on YTD value 
- Answer in Thai