
CREATE TABLE "myapp_bookproduct" (
	"id"	integer NOT NULL,
	"bookname"	varchar(100) NOT NULL,
	"price"	varchar(100) NOT NULL,
	"author"	varchar(100) NOT NULL,
	"description"	varchar(500),
	"imageurl"	varchar(500),
	"imagefilename"	varchar(500),
	"instock"	bool NOT NULL,
	"unit"	varchar(200) NOT NULL,
	"quantity"	integer NOT NULL,
	"image"	varchar(100),
	PRIMARY KEY("id" AUTOINCREMENT)
)     