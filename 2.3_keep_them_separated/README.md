## 2.3 Keep them separated

Moved the **Log output** and **Ping pong** applications to a dedicated namespace called `exercises`.

### Usage

**1. Create Namespace**

```bash
kubectl create namespace exercises
```

**2. Build Images**

```bash
docker build -t src-1-log-output:v1 ./2.3_keep_them_separated/src_1_log_output/
docker build -t src-2-pingpong:v1 ./2.3_keep_them_separated/src_2_pingpong/
```

**3. Deploy**

```bash
kubectl apply -f ./2.3_keep_them_separated/manifest/
```
