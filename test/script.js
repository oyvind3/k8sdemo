import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  stages: [
    { duration: '1m', target: 100 }, // ramp up to 1000 VUs over 10 minutes
    { duration: '5m', target: 100 }, // stay at 1000 VUs for 10 minutes
    { duration: '2m', target: 0 }, // ramp down to 0 VUs over 10 minutes
  ],
};

export default function () {
  http.get('');
  sleep(1);
}
