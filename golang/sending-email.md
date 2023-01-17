## SMTP

Requires actual email credentials which may lead to various security-related concerns. Not recommended.

```go
package controller

import (
	"errors"
	"fmt"
	"net/smtp"
	"portfolio_golang/src/config"
	e "portfolio_golang/src/errors"

	"github.com/gin-gonic/gin"
)

type SmtpServer struct {
	host string
	port string
}

type loginAuth struct {
	USERNAME string
	PASSWORD string
}

func LoginAuth(username, password string) smtp.Auth {
	return &loginAuth{username, password}
}

func (a *loginAuth) Start(server *smtp.ServerInfo) (string, []byte, error) {
	return "LOGIN", []byte{}, nil
}

func (a *loginAuth) Next(fromServer []byte, more bool) ([]byte, error) {
	if more {
		switch string(fromServer) {
		case "Username:":
			return []byte(a.USERNAME), nil
		case "Password:":
			return []byte(a.PASSWORD), nil
		default:
			return nil, errors.New("Unknown fromServer")
		}
	}
	return nil, nil
}

func SendEmail(c *gin.Context, appCfg *config.EnvConf, receivers []string, msg []byte) bool {
	auth := LoginAuth(appCfg.SMTPADDRESS, appCfg.SMTPPASSWORD)

	err := smtp.SendMail("smtp.gmail.com:587", auth, "daronphang22@gmail.com", receivers, msg)
	if err != nil {
		err := e.NewError(
			e.ErrSendMail,
			fmt.Sprintf("unable to send email to %s with message %s", receivers, msg),
			c.HandlerName(),
		)
		c.Error(err).SetMeta(err.Meta())
		return false
	}
	return true
}
```

## Gmail API

https://articles.wesionary.team/sending-emails-with-go-golang-using-smtp-gmail-and-oauth2-185ee12ab306

https://console.cloud.google.com

```go

```
