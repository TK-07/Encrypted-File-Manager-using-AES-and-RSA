# Encrypted-File-Manager-using-AES-and-RSA


Thamarai Kannan P , Yuva Rani V H , Nirmala R , PG scholar, SCOPE, VIT University, Vellore, India


Maintaining file manager is essential for ordering and accessing files in ease. But a file resides in local file manager cannot be accessed from other devices. Uploading that file on cloud creates a major risk when an unencrypted file having sensitive data got on hands of attacker when cloud storage account is compromised. So an approach is required to maintain files in an secured cloud environment which can be accessed by user from any device. Maintaining Encrypted File Managers on cloud could be optimal solution.  The file manager on cloud acts like a repository which stores user's sensitive files that can be accessed by user with a single Master Password. To secure the files in such environment various Encryption and Decryption techniques are need to be carried out. There are various encryption and decryption algorithm that are classified to many types based on various constraints such as , based on Data being encryption , Mathematical function used , type of Keys used etc ..,. Some of these types are Symmetric and Asymmetric algorithms which are classified based on keys used. The Bit cipher and Block cipher algorithms that are classified based on data they have been encrypting. Some of famous Encryption and Decryption algorithms are DES (data encryption standard) , Blow fish , Two fish , Triple DES , AES , RSA etc..,. Here AES , DES and Triple DES are block cipher based algorithm that process the data as blocks and uses Symmetric keys for these process. RSA on the other hand is an Asymmetric key algorithm that uses completely different keys for encryption and decryption .These algorithm have to be chose wisely based on application to give an efficient intended results. For storing and retrieving a file from cloud an effective cloud environment needs to be implemented that can co-operatively work with any kind of applications . In such a case the reliable cloud storage environment is mandatory such as Amazon SSS, Google firebase, Azure cloud storage, etc..,.

AES and RSA algorithm can be used to secure file manager on cloud. Advanced Encryption Standard (AES) is a symmetric-key algorithm, in which the same key is used for both encrypting and decrypting the data. AES have fixed block size of 128 bits with key size is 128, 192, 256 and rounds is 10, 12, 14 (its depending on key size). They are used for increase data security and confidentiality. RSA (Rivest–Shamir–Adleman) is an asymmetric cryptographic algorithm, in which they use two different keys and the key size is 1,536 to 4,096 bit with round 1. It is used to encrypt the data to provide security so that only the concerned user can access it. By securing the data, we are not allowing unauthorized access to it. User data is encrypted first and then it is stored in the Cloud. When user places a request for the data in the Cloud . The data is provided to respected user by decryption after accepting Master key from user. Double encryption process will take place to enhance the security where the data that are encrypted by using AES will produce a Master key. The AES Master key again encrypted by RSA  which produce another key and the key needs to be maintained securely. During decryption, the  RSA key is used to decrypt AES Master key and at last by using AES Master key the data is decrypted and viewed by user. The data here represents the user's files. The proposed system can be implemented by using an Google Firebase cloud that can be accessed through an API calls. 


<br>

<img src="File manager.jpeg">





