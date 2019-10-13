import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {HttpParams} from "@angular/common/http";
import {NgForm} from '@angular/forms';
import { ToastController } from '@ionic/angular';

@Component({
  selector: 'app-schedule',
  templateUrl: './schedule.component.html',
  styleUrls: ['./schedule.component.scss'],
})
export class ScheduleComponent implements OnInit {
  curDate=new Date();

  constructor(private http:HttpClient, public toastController: ToastController) { }

  ngOnInit() {}

  onSubmit(f: NgForm) {
    console.log(f.value);  
    // console.log(f.valid);  // false
    this.http.post("http://hack.thedevbin.com:9000/scheduleEvent",
    {
      data: f.value
    }).subscribe(() => { // * not callback
      this.showToast("Scheduled a start time");
      console.log(`ahhhhhhh`); 
    }, error => {
      this.showToast("There was an error");
      console.log("Error", error);
    });
    
  }
  showToast(messageStuff) {
    this.toastController.create({
      message: messageStuff,
      duration: 2000,
      animated: true,
      showCloseButton: true,
      closeButtonText: "OK",
      cssClass: "my-toast",
      position: "bottom"
    }).then((obj) => {
      obj.present();
    });
  }
}
