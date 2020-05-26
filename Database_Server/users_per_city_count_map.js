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
