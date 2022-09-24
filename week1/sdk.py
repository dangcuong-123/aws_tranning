import boto3 

ec2 = boto3.client("ec2")
response = ec2.run_instances(
	imageId="ami-03f4fa076d2981b45,"
	InstanceType="t2.micro",
	MinCount=1,
	MaxCount=1,
	KeyName="cuong_aws",
)


