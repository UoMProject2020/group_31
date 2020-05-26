//--------------------------------
//Group No. 31
//Team Members
//Akshay Agarwal, 1141290,Melbourne
//Avi Patel,1143213,Melbourne
//Monit Patel,1135025,Melbourne
//Prabha Choudhary,1098776,Melbourne
//Shubham Parakh,1098807,Melbourne
//--------------------------------

function(doc) { 
	if(doc.user.location.toLowerCase().includes("melbourne"))
		{
		emit(["melbourne",doc.user.id],1);
		}
	else if (doc.user.location.toLowerCase().includes("sydney"))
		{
		emit(["sydney",doc.user.id],1);
		}
	else if (doc.user.location.toLowerCase().includes("adelaide"))
		{
		emit(["adelaide",doc.user.id],1);
		}
	else if (doc.user.location.toLowerCase().includes("brisbane"))
		{
		emit(["brisbane",doc.user.id],1);
		}
	else if (doc.user.location.toLowerCase().includes("canberra"))
		{
		emit(["canberra",doc.user.id],1);
		}
	else if (doc.user.location.toLowerCase().includes("darwin"))
		{
		emit(["darwin",doc.user.id],1);
		}
	else if (doc.user.location.toLowerCase().includes("hobart"))
		{
		emit(["hobart",doc.user.id],1);
		}
	else if (doc.user.location.toLowerCase().includes("perth"))
		{
		emit(["perth",doc.user.id],1);
		}
	else
		{
		emit(["unknown",doc.user.id],1);
		}
	}
