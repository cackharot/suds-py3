using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.ServiceModel;
using System.ServiceModel.Description;
using System.IdentityModel.Selectors;
using System.Net;
using System.ServiceModel.Security;

namespace Cackharot.SampleSoapService
{
    [ServiceContract]
    public interface IHelloService
    {
        [OperationContract]
        string sayHello(string name);

        [OperationContract]
        double add(double a, double b);
    }

    public class HelloService : IHelloService
    {
        public string sayHello(string name)
        {
            return string.Format("Hello {0}!", name);
        }

        public double add(double a, double b)
        {
            return a + b;
        }
    }

    public class CustomUserNamePasswordValidator : UserNamePasswordValidator
    {
        public override void Validate(string userName, string password)
        {
            if (!("bob".Equals(userName) && "catbob".Equals(password)))
            {
                throw new FaultException("Invalid username or password");
            }
        }
    }

    public class Program
    {
        public static void Main(string[] args)
        {
            string url = "http://localhost:8181/soap/helloservice";
            ServiceHost serviceHost = null;

            try
            {
                serviceHost = new ServiceHost(typeof(HelloService), new Uri(url));
                
                var smb = new ServiceMetadataBehavior();
                smb.HttpGetEnabled = true;
                serviceHost.Description.Behaviors.Add(smb);

                serviceHost.Credentials.UserNameAuthentication.UserNamePasswordValidationMode = UserNamePasswordValidationMode.Custom;
                serviceHost.Credentials.UserNameAuthentication.CustomUserNamePasswordValidator = new CustomUserNamePasswordValidator();

                serviceHost.AddServiceEndpoint(ServiceMetadataBehavior.MexContractName, MetadataExchangeBindings.CreateMexHttpBinding(), "mex");
                var binding = new BasicHttpBinding(BasicHttpSecurityMode.TransportCredentialOnly);
                binding.Security.Transport.ClientCredentialType = HttpClientCredentialType.Basic;
                serviceHost.AddServiceEndpoint(typeof(IHelloService), binding, string.Empty);
                serviceHost.Open();

                var endpoint = serviceHost.Description.Endpoints.First();
                Console.WriteLine("The Hello service is running and is listening on:");
                Console.WriteLine("{0} ({1})", endpoint.Address.ToString(), endpoint.Binding.Name);
                Console.WriteLine("\nPress any key to stop the service.");
                Console.ReadKey();
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }
            finally
            {
                if (serviceHost != null)
                {
                    if (serviceHost.State == CommunicationState.Faulted)
                    {
                        serviceHost.Abort();
                    }
                    else
                    {
                        serviceHost.Close();
                    }
                }
            }
        }
    }
}