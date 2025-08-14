import boto3
s3 = boto3.client("s3")
for b in s3.list_buckets().get("Buckets", []):
    name = b["Name"]
    print(f"[Bucket] {name}")
    try:
        acl = s3.get_bucket_acl(Bucket=name)
        print(" ACL grantees:", [g['Grantee'].get('URI') or g['Grantee'].get('ID') for g in acl['Grants']])
    except Exception as e:
        print(" ACL error:", e)
