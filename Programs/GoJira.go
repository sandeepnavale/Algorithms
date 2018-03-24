package main

import (
	"fmt"

	"github.com/andygrunwald/go-jira"
)

func main() {
	tp := jira.BasicAuthTransport{
		Username: "nsandeep",
		Password: "$unny1nAUS",
	}

	client, err := jira.NewClient(tp.Client(), "https://dev.pulsesecure.net/jira/")

	u, _, err := client.User.Get("nsandeep")
	fmt.Println(u.Name)

	// fmt.Printf("\nEmail: %v\nSuccess!\n %d ", u.EmailAddress, err)
}
