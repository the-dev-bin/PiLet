import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {HttpParams} from "@angular/common/http";
import {NgForm} from '@angular/forms';

@Component({
  selector: 'app-schedule',
  templateUrl: './schedule.component.html',
  styleUrls: ['./schedule.component.scss'],
})
export class ScheduleComponent implements OnInit {
  curDate=new Date();

  constructor(private http:HttpClient) { }

  ngOnInit() {}

  onSubmit(f: NgForm) {
    console.log(f.value);  // { first: '', last: '' }
    console.log(f.valid);  // false
    this.http.post("http://hack.thedevbin.com:9000/test",
    {
      data: f.value
    })
  }
}
