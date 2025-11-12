# Deployment Guide — OCI Functions + API Gateway

## 1. Objective
Deploy a simple serverless API using Oracle Cloud Infrastructure (OCI)
Functions (Python and Node.js) behind an API Gateway.

## 2. Prerequisites
- Oracle Cloud account (Free tier is fine)
- OCI CLI installed and configured
- Postman for testing
- GitHub account for version control

## 3. Steps
1. **Create an OCI Function Application**
   - Name: `integration-demo`
2. **Deploy Functions**
   - Zip `python-function` and `node-function` separately.
   - Deploy using OCI CLI:  
     `fn deploy --app integration-demo`
3. **Create API Gateway**
   - Create Deployment → Add routes:
     - `/python/hello` → Python function
     - `/node/hello` → Node function
4. **Test in Postman**
   - Use provided collection under `/postman/`
5. **Monitor Logs**
   - Navigate: Developer Services → Functions → Logs.
