##### exported by Trello Parser on 2020-01-17 17:52:27.718436 #####

---
### BACKLOG
---
- Bonifici Cornèrtrader
- CM, attivare Dynatrace
- Aggancio relazione Dynacos in modalità Self Service
- Credit Lombard - `Nuova sezione App per investimenti. Da fare per ora analisi, stima, plan di alto livello. `
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Previsto con COLN e BIGN un momento di verifica / stima MARTEDI 21.1</span>
- Upselling - `Esperimento
Es: acquisto di un nuovo prodotto
Stile "shop", carrello della spesa`
  - [PELM - 2020.1.9] stime attorno ai 250 gu (2 mesi di elapsed, 3FE + 2BE)
- Onboarding
  - [PELM - 2020.1.9] stima fatta, 650 gu per la parte di BE + FE, Sketchin come UX design, MSSL come "wrapper" di tutte le funzionalità (no integrazione con CMOD, OpenCMS, ...)
- Visualizzazioni titoli di portafoglio (SIPA ONLINE) - `In standby`
- News 2 Trading - `Da un dettaglio di una news finanziaria permettere all'utente di passare al dettaglio dello stesso titolo per comprare`
- Ottimizzazione performances Tab Banca
- Batches - Fixes
- Pulizia PushID Firebase
- Documentazione Brain Aux CC
- Documentazione CNS Delivery
- Dashboard Splunk CNS Delivery
- Pulizia dati Ricerca Finanziaria

---
### READY
---
- Migrazione OASIS -> OSM
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Nulla di nuovo questa settimana</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Con Liviana andiamo un po' a rilento. Ci si trova a fine gennaio per organizzare l'inizio degli sviluppi, che seguirà Enrico Visentin (supervisione NAPS). 
</span>
- SAXO - Dynamic Certificate Loading - `In standby fino a Febbraio`
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17]  Visentin deve completare l'attività al rientro. Per ora è in recupero operazione.</span>
- Attivazione ambiente di PREP WellD

---
### IN PROGRESS
---
- TdP - Polizze - API di BE
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Alberto questa settimana ha completato l'inserimento delle polizze rosse. Dovrebbe essere finito. Sta procedendo con la validazione dei campi di input. Abbiamo smarcato con Carmine uno use case non chiaro (IBAN presente / assente nelle polizze e relativo recupero Clearing). Su suo suggerimento, abbiamo riaperto Confluence come spazio per la documentazione accessibile anche da fuori. Ha segnalato qualche problema con l'avvio del COR da VDI, viene in settimana a verificare con BIGN l'avvio. Altro problemino, l'utenza tecnica BMS non è allineata all'utenza tecnica COR, sto provando a riallinearla (vedi nota su dismissione DB2)</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Le attività di BE procedono, con il nuovo Sprint Alberto si sta dedicando alla validazione dei campi dei pagamenti. Rimangono ancora 2 macro capitoli: strong authorization e listati. Previsto Assessment di sicurezza, indicativamente dopo Pasqua (15.4). Necessario l'intervento di DIMA per testare l'immissione dei pagamenti, troppe le incertezze del caso, chiesto a COLN di organizzare per I primi di marzo.  </span>
- TdP - Polizze e attività di FE
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Alla demo (sprint 39) abbiamo visto il flusso di abilitazione device ai pagamenti completato, lo sprint si è concluso bene. Prossimi step le validazioni sui campi e inizio aggancio alle api di BE</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Le attività di FE vanno avanti, questo sprint sono state disegnate le schermate di autorizzazione, ma il flusso ancora non è collegato (manca il BE). Il prossimo sprint faremo I settings e sistemereo l'immissione dei pagamenti. </span>
- TdP - Polizze e attività di QA
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Con Francesco, ci siamo concentrati a costruire la prima suite di test, quella "generica" per verificare la bontà di un deployment. A questa seguirà quella sui casi di QA pagamenti. Occorre ancora tutto lo sprint in corso per completare.</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Le attività di QA procedono, ho chiesto di avere 3 suite di test: 1 per un flusso "generico" di validazione BE, per verificare che tutti gli endpoint funzionano e ritornano dati strutturalmente corretti, 1 per verificare il WAF (deve tornare errori coerenti ad ogni rilascio), 3 per verificare gli use case, soprattutto per il traffico dei pagamenti.</span>
- TdP - Strong Authorization pagamenti
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Pingato Nicolas per avere un OK ad inviare il documento alla security. 
</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Il documento di Strong Authorization è praticamente finito, occorre completarlo (4 / 6h) e consegnarlo alla Security per una validazione.</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.16] Documento  completato, consegnato a Nicolas per revisione. In attesa di suo ok, per mandarlo alla security</span>
- TdP - QR Fattura
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] COLN ha chiesto di implementare già a Giugno la QR fattura --> 30.4 sviluppi Dynacos pronti... sarà difficile targetizzare giugno!! Siamo comunque fermi per ora... non abbiamo risorse per curare OGGI anche questo tema (si pensava lo facesse il COR...). Decisione ancora da prendere.</span>
- Dismissione DB2 / DB alternativo - `In standby fino a febbraio 2020`
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Ho completato il merge delle tabelle myCornèr e Cornèronline (vedi mail in esterna). Ancora qualche ora con BIGN e la tabella è completa.</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Dovevamo incontrarci la prima di gennaio, ma abbiamo concordato con COLN di rinviare a febbraio (al ritorno di NAPS) l'incontro, per poterlo fare bene e iniziare a pianificare le attività.
</span>
- Push SAXO
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Stretto contatto con Salezze, i test sono andati bene. Qualche piccola correzione e il desiderio di fare qualche test in più, ma tutto ok. Attendiamo lunedi il documento con i commenti. Quando torna NAPS finalizziamo e apriamo in PROD ma in modalità F&F (Salezze di nuovo..)</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Abbiamo completato il BE. Dato a Salezze un telefono di prova per validate gli Use Case (documento di specifiche funzionali alla mano). Mancano probabilmente solo I testi, per ora li abbiamo inventati noi, sicuramente saranno da cambiare. </span>
- Sketchin, tab bar con loghi
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Non ho news...</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.16] Nicolas ha ingaggiato Sketchin per provare a verificare una main bar (quella in basso) che presenti i loghi dei prodotti. In attesa.</span>
- Adobe Analytics
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Per ora deprioritizzato, messo nei prossimi sprint</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Analytics di base pronte su app CH. App BS ancora da verificare. In attesa di poter implementare il tracking dei pagamenti nei prossimi sprint. </span>
- QA - Test E2E per FE
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.10] comunicata a WellD l'esigenza di avere e2e che coprono gli use case dell'app, con priorità al traffico dei pagamenti. Ci si riflette un attimo su e si ragiona insieme martedi prox per capire cosa fare (dipende da quanto costa)</span>
- Release Train
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Nulla di nuovo questa settimana</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Qualcosa ancora non va.. MOMA mi rifiuta I deploy in urgenza "perchè nessuno gli ha detto nulla"...
</span>
- Messa in sicurezza accessi a Firebase - `In standby, in attesa del comitato di sicurezza`
  - [PELM - 2020.1.7] Ad oggi, nessun feedback
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Ricevuta mail di Orlando, il quale riferisce che Enea ne vuole parlare al Comitato di Sicurezza</span>
- Supporto a Team Cornèronline
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Questa settimana l'ho visto meglio, anche la collaborazione con Federico mi sembra funzionare meglio. Piccoli progressi.</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Visentin deve completare ancora integrazione SSO con SPNEGO, ma fa fatica... </span>

---
### DONE
---
- Tab Banca su Servizi MSSL
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Verificato con TestFlight, funziona. Peccato per la necessità di un nuovo TestFlight... attendiamo apertura per chiudere il task</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Bug risolto. Deploiato BE in PROD, in attesa di Test Flight definitivo per poter aprire al pubblico.</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Bug filtraggio amount non ancora risolto, ci sta guardando Tiziano. Per il resto, utenti aperti, per ora sembra mantenuta costante la velocità, ma sembra per un problema di "codice legacy" (per un utente con 2 relazioni e 2 conti, ci sono 7 chiamate da fare.. Ne basterebbe 1... Debito tecnico da sanare, non so quando avremo tempo di guardarci... </span>
- HELPONLINE - bug su Area News active ma senza accessi

---
### IN STANDBY
---
- CI mobile apps
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Discusse varie possibilità: 
- mantenere soluzione AS-IS e pagare servizio
- rollback su build a mano (NO!)
- portare in casa la CI, con INSI, PATM, NAPS, CONF, ... sembra la strada fattibile</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Vi sono margini di miglioramento..  
https://nevercode.io/blog/how-to-implement-continuous-delivery-for-mobile-app-development-insights-from-authentiq/</span>
- Aggiornamento Kubernates - `In standby fino a ritorno di NAPS`
  - [PELM - 2020.1.7] CNS delivery BS deve prima essere aggiornato a CH
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Nulla di nuovo</span>
- R2020 - SecureAccess - `In standby, finchè non torna NAPS`
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Sviluppi completati, manca "IF DI BASI", previsto per febbraio. Contiamo di andare in prod per la fine di febbraio, per poi essere pronti a testare l'ambiente "I" a target.</span>
- R2020 - Test myCornèr (rimorchio features) - `In standby`
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Rimane da capire "praticamente" date e modalità con cui dobbiamo andare a provare l'integrazione SecureAccess "nuovo" in DEV/TEST (ambiente I) e in PREP (M1). Poi pronti a F&F, anche qui da formalizzare per bene tempi e modalità.</span>
- WAF FIX - `In standby, finchè non torna RICE`
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Sembra che i fix siano OK. Col fatto che RICE è in vacanza, attendiamo il ritorno per provare nuovamente tutto in PREP e poi schedulare il rilascio in PROD per metà Febbraio.</span>
- Dismissione myCornèr 1.x - `Standby fino a febbraio 2020`
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Storie inserite a Backlog</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Standby fino a febbraio 2020</span>
- Aggiornamento driver DB2 - `In standby finchè non torna NAPS, poi riattiviamo`
- Ambienti Dynacos
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] si sta muovendo anche Liviana, con fede.. ma non vi è discorso "unico". Per ora in attesa di incontro con VASCO su procedura CREAT. Quando torna NAPS proviamo a deploiare in TEST puntanto a K e G, vediamo che succede.</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Inviato agli stakeholders la proposta per la modifica CREAT, ma non ho avuto risposta. Invece siamo pronti per testare il deploy in TEST e PREP sugli ambienti alternativi (K, G, O, …), le utenze sono state create.
</span>
- FINMA - `In standby`
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Giusto una nota, sembra che arriveranno a breve indicazioni di cosa vuol dire "essere compliant alla FINMA" anche su CB. In attesa. </span>

---
### VARIE ED EVENTUALI
---
- Project
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Cosa facciamo?</span>
- Fatture
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] In attesa delle fatture di gennaio</span>
- Alexa - `In standby, in attesa di CAVL`
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Incontro 21.2 con CAVL, BORS, COLN per capire come andare avanti</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Pino insiste per fare cose... per ora ho temporeggiato fino al ritorno di NAPS, ma non abbiamo molto agio... VICO però se l'aspetta... verifico con CAVL che piano ha...</span>
- Lightning Decision Jam - Information Radiator
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Impostata la board Jira secondo quanto permette il plugin, questa settimana non ho avuto tempo per completare per bene, ma manca poco.</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Andreas ha trovato un ottimo plugin Jira, che fa esattamente quello che è richiesto. Ma è a pagamento e non costa poco... ma, colpo di coda, ci siamo accorti che Jira di default offre una funzionalità di base molto interessante, la WallBoard.. Nel Weekend facciamo qualche prova e vediamo di capire come completare questo task senza spendere un franco. Ci serve un monitor grande :) </span>
- Lightning Decision Jam - SCRUM process
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] Questa settimana ho impostato i meeting secondo calendario, rivisto alcuni aspetti del processo (prioritizzazione, gestione del bug).</span>
  - <span style="color:blue; font-weight:bold;"> [PELM - 2020.1.17] su tema Qualità / Velocità abbiamo fatto il secondo incontro Light Decision Jam e "mi sono portato a casa" I seguenti task:  
- Diffondere e applicare la metodologia AGILE nel team, spiegandone le regole 
- Organizzare I calendari (e farli rispettare) 
- Uniformare il processo AGILE tra I team (almeno tra MYC e CMA)</span>

---
### Cosa mi lascia NAPS
---
- CREAT 403838: apertura websocket - pre-proxy SAXO in PROD
- CREAT 403928: credenziali mancanti (CNS Loader + Brain SAXO in PREP + CNS Delivery (credenziali di accesso) per il BRAIN di PROD)
- CREAT 403981: creazione tabella distributed lock per la PROD
- fare creat per GRANT distributed lock x Loader in TEST / PREP / PROD
- CREAT 403948: GRANT 4/5 tabelle per BRAIN in TEST / PREP / PROD
- CREAT 403911: promuove la tabella distributed lock in PREP --> serve fare anche quello per la PROD
- Settings SAXO BE fatto

---
### Lokalise
---
