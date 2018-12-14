# Nordic Car Rental
Verklegt námskeið 1

## Authors
- Ásta Gísladóttir
- Elín Hrund Búadóttir
- Pétur Aron Sigurðsson
- Sindri Snæfells Kristinsson

Við uppsetningu á forritunu höfum við fylgt lagskiptingu (layering):
1. presentation layer		
Main		
Þrír Ui klasar (Customer, Car, Booking)		
		
2. domain layer		
Service og models (Customer, Car, Booking)		
		
3. data layer		
Repositories (Customer, Car, Booking)		
txt skrár í data (Customer, Car, Booking, Price)		
		
Klasarnir tengjast frá models inn í repositories, þaðan í service, þaðan í Ui og að lokum þaðan í main. Hver klasaflokkur fer í gegnum þessi lög og haldast tengingar innan flokkana þangað til komið er í main.		
		
Mikilvægt er við keyrslu á kerfinu að skrárnar customer.txt, car.txt, booking.txt og price.txt séu til staðar.		
		
Slóð á kóða á github:		
https://github.com/peturs17/carRental		
