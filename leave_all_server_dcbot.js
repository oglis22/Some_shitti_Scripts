//Lasse deinen Bot von jedem server leaven

const { Client, GatewayIntentBits } = require('discord.js');                                                                                                               
                                                                                                                                                                                                                                                                                                      
const TOKEN = 'MTIzODI2NjI4ODY4MjMwMzU1OQ.Gh_pGp.51G4I9mQ2uHUyZ7hDYO1d5mPBYdDzntDq1jBdU';                                                                                  
                                                                                                                                                                                                                                                                                                             
const client = new Client({ intents: [GatewayIntentBits.Guilds] });                                                                                                        
                                                                                                                                                                                                                                                                                                           
client.once('ready', async () => {                                                                                                                                         
  console.log(`Bot ist eingeloggt als ${client.user.tag}`);                                                                                                                
                                                                                                                                                                                                                                                                                         
  for (const guild of client.guilds.cache.values()) {                                                                                                                      
    try {                                                                                                                                                                  
      await guild.leave();                                                                                                                                                 
      console.log(`Bot hat den Server "${guild.name}" verlassen.`);                                                                                                        
    } catch (error) {                                                                                                                                                      
      console.error(`Fehler beim Verlassen des Servers "${guild.name}":`, error);                                                                                          
    }                                                                                                                                                                      
  }                                                                                                                                                                        
                                                                                                                                                                                                                                                                                 
  client.destroy();                                                                                                                                                        
});                                                                                                                                                                        
                                                                                                                                                                           
// Bot anmelden                                                                                                                                                            
client.login(TOKEN).catch(error => {                                                                                                                                       
  console.error('Fehler beim Einloggen:', error);                                                                                                                          
});                    
