Sample use of mountebank-mocks-manager

Here simple setup is prepared:

1. Two applications, Alice and Bob. 
2. Alice receives data from Bob.
3. Alice is connected with Bob via mountebank instance.
4. In the proxy mode Alice sends request to Bob using mountebank, receives response. MMM processes data and creates mocks basing on request/response stored in automatic mode.
5. In mocks mode Alice thinks that she sends request to Bob, meanwhile it sends request and receives response from mountebank.
