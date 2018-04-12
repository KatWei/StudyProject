<?php

namespace App\Models;

use Illuminate\Notifications\Notifiable;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Support\Facades\Auth;
use Spatie\Permission\Traits\HasRoles;

/**
 * Class User
 *
 * @package App\Models
 */
class User extends Authenticatable
{
    use Traits\ActiveUserHelper;
    use Traits\LastActivedAtHelper;
    use HasRoles;
    use Notifiable {
     notify as protected laravelNotify;
    }

    /**
     * @param $instance
     */
    public function notify($instance)
    {
        if ($this->id === Auth::id()) {
            return;
        }
        $this->increment('notification_count');
        $this->laravelNotify($instance);
    }

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name', 'email', 'password', 'introduction', 'avatar'
    ];

    /**
     * The attributes that should be hidden for arrays.
     *
     * @var array
     */
    protected $hidden = [
        'password', 'remember_token',
    ];

    /**
     * @return \Illuminate\Database\Eloquent\Relations\HasMany
     */
    public function topics()
    {
        return $this->hasMany(Topic::class);
    }

    /**
     * @return \Illuminate\Database\Eloquent\Relations\HasMany
     */
    public function replies()
    {
        return $this->hasMany(Reply::class);
    }

    /**
     * @param $model
     *
     * @return bool
     */
    public function isAuthorOf($model)
    {
        return $this->id == $model->user_id;
    }

    /**
     * @param $value
     */
    public function setPasswordAttribute($value)
    {
        if (strlen($value) != 60) {
            $value = bcrypt($value);
        }

        $this->attributes['password'] = $value;
    }

    public function setAvatarAttribute($path)
    {
        if (!starts_with($path, 'http')) {
            $path = config('app.url').'/uploads/images/avatar/$path';
        }
        $this->attributes['avatar'] = $path;
    }

    public function markAsRead()
    {
        $this->notification_count = 0;
        $this->save();
        $this->unreadNotifications->markAsRead();
    }


}
