# route53_failover_tester.py
import boto3

client = boto3.client('route53')
health = client.list_health_checks()

for hc in health['HealthChecks']:
    status = client.get_health_check_status(HealthCheckId=hc['Id'])
    print(f"{hc['HealthCheckConfig']['FullyQualifiedDomainName']}: {status['HealthCheckObservations'][0]['StatusReport']['Status']}")