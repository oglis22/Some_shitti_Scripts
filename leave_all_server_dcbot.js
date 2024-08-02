//Lasse deinen Bot von jedem server leaven

const { Client, GatewayIntentBits } = require('discord.js');                                                                                                               
                                                                                                                                                                                                                                                                                                      
const TOKEN = '';                                                                                  
                                                                                                                                                                                                                                                                                                             
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
