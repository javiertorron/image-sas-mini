export class TokenResponseDTO {
  access_token: string;
  token_type: string;
  
  constructor(access_token: string, token_type: string) {
    console.log(`Constructor: ${access_token}`)
    this.access_token = access_token;
    this.token_type = token_type;
  }
}