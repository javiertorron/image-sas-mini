export class TokenResponseDTO {
    token: string;
    type: string;
  
    constructor(access_token: string, token_type: string) {
      this.token = access_token;
      this.type = token_type;
    }
  }