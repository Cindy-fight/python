import oss2

auth = oss2.Auth('LTAIKdjn445KIAfy', 'd78fFsDltKYIRC5mrsP6yIvGbtWshb')

bucket = oss2.Bucket(auth, 'mgwebsite.oss-cn-shanghai.aliyuncs.com', 'mgwebsite')

bucket.create_bucket()