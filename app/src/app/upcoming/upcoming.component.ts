import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-upcoming',
  templateUrl: './upcoming.component.html',
  styleUrls: ['./upcoming.component.scss'],
})
export class UpcomingComponent implements OnInit {
  
  dataStuff = {}

  public arrayOfKeys;

  constructor(private http:HttpClient) {

    this.http.get("http://localhost:9000/getSchedule").subscribe(data => this.updateData(data));
    this.arrayOfKeys = Object.keys(this.dataStuff);
   }

   updateData(stuff){
     this.dataStuff = stuff;
    //  console.log(this.dataStuff);
   }

  ngOnInit() {}

}
